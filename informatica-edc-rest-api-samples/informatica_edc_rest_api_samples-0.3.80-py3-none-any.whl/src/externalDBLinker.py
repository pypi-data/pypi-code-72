"""
Created on Aug 7, 2018

@author: dwrigley

resolve links for External Database/Schema objects
write a custom lineage file to import the links
or
options include to create links directly (via API) - via -i switch (or --edcImport)

"""
import json
import csv
from src.edc_utilities import edcSessionHelper, edcutils
import time
import sys
import argparse
import urllib3
import os

urllib3.disable_warnings()

# set edc helper session + variables (easy/re-useable connection to edc api)
edcHelper = edcSessionHelper.EDCSession()

# define script command-line parameters (in global scope for gooey/wooey)
parser = argparse.ArgumentParser(parents=[edcHelper.argparser])

# add args specific to this utility (left/right resource, schema, classtype...)
parser.add_argument(
    "-f",
    "--csv_file_name",
    default="dbms_externalDBLinks.csv",
    required=False,
    help=(
        "csv file to create/write (no folder) default=dbms_externalDBLinks.csv "
    ),
)
parser.add_argument(
    "-o",
    "--outDir",
    default="out",
    required=False,
    help=(
        "output folder to write results - default = ./out "
        " - will create folder if it does not exist"
    ),
)

parser.add_argument(
    "-i",
    "--edcimport",
    default=False,
    # type=bool,
    action='store_true',
    help=(
        "use the rest api to create the custom lineage resource and start the import process "
    ),
)

parser.add_argument(
    "-rn",
    "--lineageResourceName",
    default="externalDBlinker_lineage",
    required=False,
    help=(
        "custom lineage resource name to create/update - default value=externalDBlinker_lineage"
    ),
)
parser.add_argument(
    "-rt",
    "--lineageResourceTemplate",
    default="template/custom_lineage_template.json",
    required=False,
    help=(
        "custom lineage resource template (json format) use for creating a new resource - default value=template/custom_lineage_template.json"
    ),
)

# waitToComplete setting is not active (and probably not useful anyway)
waitToComplete = False


def getColumnsForTable(tableId):
    """
    get all columns for a table and return in a dict key=column name
    (lowercase) val=column id
    use the GET /access/2/catalog/data/objects id=tableId
    look for columns via com.infa.ldm.relational.TableColumn
          or com.infa.ldm.relational.ViewViewColumn relationship type

    """
    # TODO: this could be moved to edcutils.py?

    print("\t\t\tget cols for table:" + tableId)
    parameters = {
        "id": tableId,
        "offset": 0,
        "pageSize": 1,
    }  # pagesize can be 1 - since we are only passing the id
    colResp = edcHelper.session.get(
        edcHelper.baseUrl + "/access/2/catalog/data/objects", params=parameters,
    )
    tableJson = colResp.json()
    # print(colResp.status_code)
    colIds = dict()
    for extDBItem in tableJson["items"]:
        # print(">>>")
        for dst in extDBItem["dstLinks"]:
            assoc = dst.get("association")
            colId = dst.get("id")
            colName = dst.get("name")
            # print("\tdst..." + assoc)
            if assoc in (
                "com.infa.ldm.relational.TableColumn",
                "com.infa.ldm.relational.ViewViewColumn",
            ):
                # key = lower_case name - for case-insensitive lookup
                colIds[colName.lower()] = colId

    return colIds


def processExternalDB(dbId, classType, dbName, resType, resName, colWriter):
    """
    dbId = the id of the external database object
    classType = the classtype of the external database oject
    dbNAme - the name of the external db object
    resType - the resource type e.g Oracle, SQLServer that created the
              external db object
    resName - the resource name that created the external db object
    colWriter - the csv File object to write any lineage entries

    process outline:-
    get lineage to the table level (2 parent/child hops) from the external database
        for each table, find the actual table that should be linked (case insensitive)
        if only 1 table was found (otherwise - print an error message)
            link the table and all columns
    """

    dbUnknown = False
    # counters for # of links created
    tabLinks = 0
    colLinks = 0
    errors = 0

    # 'External' can be used if the database name is not known (sqlserver use case)
    if dbName == "External":
        dbUnknown = True
        print("\tthe database for the externally referenced object is unknown")

    # note:  if the database type is oracle, we can't trust the name of the database
    #        since it will contain the dblink name, not the externally referenced db
    #        so we will treat it as unknown and just try to find the schema/table ref'd
    if resType == "Oracle":
        dbUnknown = True

    print(f"\ttype={classType} name={dbName} id={dbId} unknownDB:{dbUnknown}")

    # get the lineage for the database object
    lineageURL = edcHelper.baseUrl + "/access/2/catalog/data/relationships"
    lineageParms = {
        "seed": dbId,
        "association": "core.ParentChild",
        "depth": "2",
        "direction": "OUT",
        "includeAttribute": {"core.name", "core.classType"},
        "includeTerms": "false",
        "removeDuplicateAggregateLinks": "false",
    }
    print(f"\tLineage query for: {dbName} params={lineageParms}")
    lineageResp = edcHelper.session.get(
        lineageURL, params=lineageParms,
    )

    lineageStatus = lineageResp.status_code
    print(f"\tlineage rc={lineageStatus}")
    lineageJson = lineageResp.text

    #  bug in the relationships api call - the items collection sould be
    #  "items" (with quotes)
    if lineageJson.startswith("{items"):
        # bug in 10.2.1 and before
        # replace items with "items" - for just the first occurrence
        # (note:  this is fixed after 10.2.1
        lineageJson = json.loads(lineageJson.replace("items", '"items"', 1))
    else:
        # 10.2.1u1 + json is escaped properly
        lineageJson = json.loads(lineageJson)

    # for each item in the lineage resultset
    for lineageItem in lineageJson["items"]:
        inId = lineageItem.get("inId")
        assocId = lineageItem.get("associationId")
        schemaName = ""
        # print("\t" + inId + " assoc=" + assocId)
        if assocId == "com.infa.ldm.relational.ExternalSchemaTable":
            # find the table...
            schemaName = inId.split("/")[-2]
            inEmbedded = lineageItem.get("inEmbedded")
            tableName = edcutils.get_fact_value(inEmbedded, "core.name")
            print(
                f"\tprocessing table={tableName} schema={schemaName}"
                f" db={dbName} id={inId}"
            )

            # format the query to find the actual table
            # "core.classType:(com.infa.ldm.relational.Table or com.infa.ldm.relational.View)  and core.name_lc_exact:"
            q = (
                "core.classType:(com.infa.ldm.relational.Table or com.infa.ldm.relational.View)  and core.name:\""
                + tableName.lower()
                + "\""
            )
            if dbUnknown and schemaName == "":
                q = q + " and core.resource_name:" + resName
            # if dbUnknown==False:
            #    q=q+ ' and ' + dbName
            q = q + ' and core.resourceType:"' + resType + '"'
            tableSearchParms = {"q": q, "offset": 0, "pageSize": 100}
            print("\t\tquery=" + str(tableSearchParms))
            # find the table - with name tableName
            tResp = edcHelper.session.get(
                edcHelper.baseUrl + "/access/2/catalog/data/objects",
                params=tableSearchParms,
            )
            tStatus = tResp.status_code
            print("\t\tquery rc=" + str(tStatus))
            # print("\t\t\t\t" + str(tResp.json()))
            foundTabId = ""
            tableMatchCount = 0
            # possible matching tables
            for tableItem in tResp.json()["items"]:
                fromTableId = tableItem["id"]
                fromSchemaName = fromTableId.split("/")[-2].lower()
                # foundTabId=''
                # foundTabId = tableItem["id"]
                # print("rs-" + fromTableId + " compared with " + inId);
                if fromTableId != inId and fromTableId.count("/") == 4:
                    # filter out comparing against itself +
                    # counting the / chars - 4 = normal db, 5=external db (disregard)
                    print("\t\tchecking " + fromTableId)
                    # print("could be this one...." + foundTabId + " << " + inId)
                    theName = fromTableId.split("/")[-1]

                    # the schema could be empty - in that case it should match dbo
                    # unless we have a way of knowing what the default schema is
                    if theName.lower() == tableName.lower() and (
                        schemaName.lower() == fromSchemaName.lower()
                        or (schemaName == "" and fromSchemaName == "dbo")
                    ):
                        tableMatchCount += 1
                        foundTabId = fromTableId
                        print(
                            f"\t\ttable name matches...{theName}=={tableName} {inId} {foundTabId} "
                            f" count/{fromTableId.count('/')}"
                        )
                    else:
                        print(
                            "\t\tno match...schema match 1:"
                            + theName
                            + " 2:"
                            + tableName
                            + " 3:"
                            + schemaName
                            + " 4:"
                            + fromSchemaName
                            + ":"
                            + str(schemaName.lower() == fromSchemaName.lower())
                        )
                # else:
                # print("skipping this one");

            print("\t\ttotal matching tables=" + str(tableMatchCount) + " inId:" + inId)
            if tableMatchCount == 1:
                # ok - we have a single table to match
                # link at the table level - then get the columns and link them too
                # print("linking from actual tab - to external ref tab")
                print("\t\tlinking tables " + foundTabId + " -->> " + inId)
                # get the columns for the ext Table
                # (will be a reduced set - only the linked columns)
                extCols = getColumnsForTable(inId)
                tabCols = getColumnsForTable(foundTabId)

                # link the table level
                edcutils.exportLineageLink(
                    foundTabId, inId, "core.DataSetDataFlow", colWriter
                )
                tabLinks += 1
                tabColsLinked = 0

                # match the columns on the left/right side
                for toCol, toId in extCols.items():
                    # check if the toCol (the name) exists in the tabCols dict
                    # print('\t\t\tchecking toCol:' + toCol + tabCols.get(toCol))
                    fromId = tabCols.get(toCol)
                    if fromId is not None:
                        # print('\t\t\tlinking columns...' + fromId + ' --->>>' + toId)
                        edcutils.exportLineageLink(
                            fromId, toId, "core.DirectionalDataFlow", colWriter
                        )
                        tabColsLinked += 1
                        colLinks += 1
                    else:
                        print(
                            f"\t\t\tError: cannot find column {toCol} in table {inId}"
                        )
                        errors += 1
                print(
                    f"\t\t\text cols:{len(extCols)} tablCols:{len(tabCols)}"
                    f" linked={tabColsLinked}"
                )
                # print("\t\t\tcolumns linked=" + str(tabColsLinked))
            else:
                print(
                    f"\t\tmutlple possible matches found ({tableMatchCount}"
                    f") no links will be created"
                )
            # flush the console buffer - for tailing the stdout log
            sys.stdout.flush()

    print(
        f"external database: {dbName} processed: tab/col links created: "
        f"{tabLinks}/{colLinks} errors:{errors}"
    )
    print("")
    return tabLinks, colLinks, errors


def main():
    """
    main starts here - run the query processing all items

    - find all com.infa.ldm.relational.ExternalDatabase objects
      - for each - call processExternalDB
    """
    print("ExternalDBLinker started")
    start_time = time.time()

    args = args, unknown = parser.parse_known_args()
    # setup edc session and catalog url - with auth in the session header,
    # by using system vars or command-line args
    edcHelper.initUrlAndSessionFromEDCSettings()
    print(f"command-line args parsed = {args} ")

    tableLinksCreated = 0
    columnLinksCreated = 0
    errorsFound = 0

    columnHeader = [
        "Association",
        "From Connection",
        "To Connection",
        "From Object",
        "To Object",
    ]
    outputFile = args.outDir + "/" + args.csv_file_name
    fullpath = os.path.abspath(outputFile)
    fCSVFile = open(outputFile, "w", newline="", encoding="utf-8")

    print("custom lineage file initialized. " + outputFile + " RELATIVE=" +fullpath)
    colWriter = csv.writer(fCSVFile)
    colWriter.writerow(columnHeader)

    parameters = {
        "q": "core.classType:com.infa.ldm.relational.ExternalDatabase",
        "offset": 0,
        "pageSize": 1000,
    }
    url = edcHelper.baseUrl + "/access/2/catalog/data/objects"

    print(
        "executing query to find all external DB objects: "
        f"{url} q={parameters.get('q')} {parameters}"
    )
    resp = edcHelper.session.get(url, params=parameters)
    status = resp.status_code
    print("extDB query rc=" + str(status))

    if status != 200:
        print(f"error - expecting 200 rc, got {status} - message={resp.json()}")
        return

    resultJson = resp.json()
    total = resultJson["metadata"]["totalCount"]
    print(f"external db objects found... {total}")
    currentDB = 0

    # for each externalDatabase object
    for extDBItem in resultJson["items"]:
        itemId = extDBItem["id"]
        currentDB += 1
        print(f"processing database: {itemId} {currentDB} of {total}")
        itemType = edcutils.get_fact_value(extDBItem, "core.classType")
        itemName = edcutils.get_fact_value(extDBItem, "core.name")
        resourceName = edcutils.get_fact_value(extDBItem, "core.resource_name")
        resourceType = edcutils.get_fact_value(extDBItem, "core.resourceType")

        tabLinks, colLinks, errors = processExternalDB(
            itemId, itemType, itemName, resourceType, resourceName, colWriter
        )
        tableLinksCreated += tabLinks
        columnLinksCreated += colLinks
        errorsFound += errors

        sys.stdout.flush()

    fCSVFile.close()
    print("finished!")
    print("table links:   created=" + str(tableLinksCreated))
    print("column links:  created=" + str(columnLinksCreated))
    print("errors found: " + str(errorsFound))

    # end of main()
    print("Finished - run time = %s seconds ---" % (time.time() - start_time))

    # call the resource create/update/load function to get the data imported into EDC
    if args.edcimport and tableLinksCreated > 0:
        edcutils.createOrUpdateAndExecuteResourceUsingSession(
            edcHelper.baseUrl,
            edcHelper.session,
            args.lineageResourceName,
            args.lineageResourceTemplate,
            args.csv_file_name,
            fullpath,
            waitToComplete,
            "LineageScanner"
        )


# call main - if not already called or used by another script
if __name__ == "__main__":
    main()
