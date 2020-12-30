import pandas as pd
import numpy as np
from collections import defaultdict


class GridOptionsBuilder:
    """Builder for gridOptions dictionary"""

    def __init__(self):
        self.__grid_options = defaultdict(dict)
        self.sideBar = {}

    @staticmethod
    def from_dataframe(dataframe):
        """
        Creates an instance and initilizes it from a dataframe.
        ColumnDefs are created based on dataframe columns and data types.

        Args:
            dataframe (pd.DataFrame): a pandas DataFrame.

        Returns:
            GridOptionsBuilder: The instance initialized from the dataframe definition.
        """

        # numpy types: 'biufcmMOSUV' https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html
        type_mapper = {
            "b": ["textColumn"],
            "i": ["numericColumn", "numberColumnFilter"],
            "u": ["numericColumn", "numberColumnFilter"],
            "f": ["numericColumn", "numberColumnFilter"],
            "c": [],
            "m": [],
            "M": ["dateColumnFilter", "shortDateTimeFormat"],
            "O": [],
            "S": [],
            "U": [],
            "V": [],
        }

        gb = GridOptionsBuilder()
        gb.configure_default_column()

        for col_name, col_type in zip(dataframe.columns, dataframe.dtypes):
            gb.configure_column(field=col_name, type=type_mapper.get(col_type.kind, []))

        return gb

    def configure_default_column(self, min_column_width=100, resizable=True, filterable=True, sorteable=True, editable=False, groupable=False, **other_default_column_properties):
        """Configure default column.

        Args:
            min_column_width (int, optional):
                Minimum column width. Defaults to 100.

            resizable (bool, optional):
                All columns will be resizable. Defaults to True.

            filterable (bool, optional):
                All columns will be filterable. Defaults to True.

            sorteable (bool, optional):
                All columns will be sorteable. Defaults to True.

            groupable (bool, optional):
                All columns will be groupable based on row values. Defaults to True.

            editable (bool, optional):
                All columns will be editable. Defaults to True.

            groupable (bool, optional):
                All columns will be groupable. Defaults to True.

            **other_default_column_properties:
                Key value pairs that will be merged to defaultColDef dict.
                Chech ag-grid documentation.
        """
        defaultColDef = {
            "minWidth": min_column_width,
            "editable": editable,
            "filter": filterable,
            "resizable": resizable,
            "sortable": sorteable,
            "enableRowGroup": groupable,
        }

        if other_default_column_properties:
            defaultColDef = {**defaultColDef, **other_default_column_properties}

        self.__grid_options["defaultColDef"] = defaultColDef

    def configure_column(self, field, header_name=None, **other_column_properties):
        """Configures an individual column
        check https://www.ag-grid.com/javascript-grid-column-properties/ for more information.

        Args:
            field (String): field name, usually equals the column header.
            header_name (String, optional): [description]. Defaults to None.
        """
        colDef = {"headerName": header_name if header_name else field, "field": field}

        if other_column_properties:
            colDef = {**colDef, **other_column_properties}

        self.__grid_options["columnDefs"][field] = colDef

    def configure_side_bar(self, filters_panel=True, columns_panel=True, defaultToolPanel=""):
        """configures the side panel of ag-grid.
           Side panels are enterprise features, please check www.ag-grid.com

        Args:
            filters_panel (bool, optional): 
                Enable filters side panel. Defaults to True.

            columns_panel (bool, optional): 
                Enable columns side panel. Defaults to True.
                
            defaultToolPanel (str, optional): The default tool panel that should open when grid renders.
                                              Either "filters" or "columns".
                                              If value is blank, panel will start closed (default)
        """
        filter_panel = {
            "id": "filters",
            "labelDefault": "Filters",
            "labelKey": "filters",
            "iconKey": "filter",
            "toolPanel": "agFiltersToolPanel",
        }

        columns_panel = {
            "id": "columns",
            "labelDefault": "Columns",
            "labelKey": "columns",
            "iconKey": "columns",
            "toolPanel": "agColumnsToolPanel",
        }

        if filters_panel or columns_panel:
            sideBar = {"toolPanels": [], "defaultToolPanel": defaultToolPanel}

            if filters_panel:
                sideBar["toolPanels"].append(filter_panel)
            if columns_panel:
                sideBar["toolPanels"].append(columns_panel)

            self.__grid_options["sideBar"] = sideBar

    def configure_selection(
        self,
        selection_mode="single",
        use_checkbox=False,
        rowMultiSelectWithClick=False,
        suppressRowDeselection=False,
        suppressRowClickSelection=False,
        groupSelectsChildren=True,
        groupSelectsFiltered=True,
    ):
        """Configure grid selection features

        Args:
            selection_mode (str, optional):
                Either 'single', 'multiple' or 'disabled'. Defaults to 'single'.

            rowMultiSelectWithClick (bool, optional):
                If False user must hold shift to multiselect. Defaults to True if selection_mode is 'multiple'.

            suppressRowDeselection (bool, optional):
                Set to true to prevent rows from being deselected if you hold down Ctrl and click the row
                (i.e. once a row is selected, it remains selected until another row is selected in its place).
                By default the grid allows deselection of rows.
                Defaults to False.

            suppressRowClickSelection (bool, optional):
                Supress row selection by clicking. Usefull for checkbox selection for instance
                Defaults to False.

            groupSelectsChildren (bool, optional):
                When rows are grouped selecting a group select all children.
                Defaults to True.

            groupSelectsFiltered (bool, optional):
                When a group is selected filtered rows are also selected.
                Defaults to True.
        """
        if selection_mode == "disabled":
            self.__grid_options.pop("rowSelection", None)
            self.__grid_options.pop("rowMultiSelectWithClick", None)
            self.__grid_options.pop("suppressRowDeselection", None)
            self.__grid_options.pop("suppressRowClickSelection", None)
            self.__grid_options.pop("groupSelectsChildren", None)
            self.__grid_options.pop("groupSelectsFiltered", None)
            return

        if use_checkbox:
            suppressRowClickSelection = True
            first_key = next(iter(self.__grid_options["columnDefs"].keys()))
            self.__grid_options["columnDefs"][first_key]["checkboxSelection"] = True

        self.__grid_options["rowSelection"] = selection_mode
        self.__grid_options["rowMultiSelectWithClick"] = rowMultiSelectWithClick
        self.__grid_options["suppressRowDeselection"] = suppressRowDeselection
        self.__grid_options["suppressRowClickSelection"] = suppressRowClickSelection
        self.__grid_options["groupSelectsChildren"] = groupSelectsChildren
        self.__grid_options["groupSelectsFiltered"] = groupSelectsChildren

    def configure_pagination(self, enabled=True, paginationAutoPageSize=True, paginationPageSize=10):
        """Configure grid's pagination features

        Args:
            enabled (bool, optional):
                Self explanatory. Defaults to True.

            paginationAutoPageSize (bool, optional):
                Calculates optimal pagination size based on grid Height. Defaults to True.

            paginationPageSize (int, optional):
                Forces page to have this number of rows per page. Defaults to 10.
        """
        if not enabled:
            self.__grid_options.pop("pagination", None)
            self.__grid_options.pop("paginationAutoPageSize", None)
            self.__grid_options.pop("paginationPageSize", None)
            return

        self.__grid_options["pagination"] = True
        if paginationAutoPageSize:
            self.__grid_options["paginationAutoPageSize"] = paginationAutoPageSize
        else:
            self.__grid_options["paginationPageSize"] = paginationPageSize

    def build(self):
        """Builds the gridOptions dictionary

        Returns:
            dict: Returns a dicionary containing the configured grid options
        """
        self.__grid_options["columnDefs"] = list(self.__grid_options["columnDefs"].values())

        return self.__grid_options
