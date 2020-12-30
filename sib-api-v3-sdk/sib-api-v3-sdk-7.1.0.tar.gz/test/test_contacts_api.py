# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import sib_api_v3_sdk
from sib_api_v3_sdk.api.contacts_api import ContactsApi  # noqa: E501
from sib_api_v3_sdk.rest import ApiException


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = sib_api_v3_sdk.api.contacts_api.ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_contact_to_list(self):
        """Test case for add_contact_to_list

        Add existing contacts to a list  # noqa: E501
        """
        pass

    def test_create_attribute(self):
        """Test case for create_attribute

        Create contact attribute  # noqa: E501
        """
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Create a contact  # noqa: E501
        """
        pass

    def test_create_doi_contact(self):
        """Test case for create_doi_contact

        Create Contact via DOI (Double-Opt-In) Flow  # noqa: E501
        """
        pass

    def test_create_folder(self):
        """Test case for create_folder

        Create a folder  # noqa: E501
        """
        pass

    def test_create_list(self):
        """Test case for create_list

        Create a list  # noqa: E501
        """
        pass

    def test_delete_attribute(self):
        """Test case for delete_attribute

        Delete an attribute  # noqa: E501
        """
        pass

    def test_delete_contact(self):
        """Test case for delete_contact

        Delete a contact  # noqa: E501
        """
        pass

    def test_delete_folder(self):
        """Test case for delete_folder

        Delete a folder (and all its lists)  # noqa: E501
        """
        pass

    def test_delete_list(self):
        """Test case for delete_list

        Delete a list  # noqa: E501
        """
        pass

    def test_get_attributes(self):
        """Test case for get_attributes

        List all attributes  # noqa: E501
        """
        pass

    def test_get_contact_info(self):
        """Test case for get_contact_info

        Get a contact's details  # noqa: E501
        """
        pass

    def test_get_contact_stats(self):
        """Test case for get_contact_stats

        Get email campaigns' statistics for a contact  # noqa: E501
        """
        pass

    def test_get_contacts(self):
        """Test case for get_contacts

        Get all the contacts  # noqa: E501
        """
        pass

    def test_get_contacts_from_list(self):
        """Test case for get_contacts_from_list

        Get contacts in a list  # noqa: E501
        """
        pass

    def test_get_folder(self):
        """Test case for get_folder

        Returns a folder's details  # noqa: E501
        """
        pass

    def test_get_folder_lists(self):
        """Test case for get_folder_lists

        Get lists in a folder  # noqa: E501
        """
        pass

    def test_get_folders(self):
        """Test case for get_folders

        Get all folders  # noqa: E501
        """
        pass

    def test_get_list(self):
        """Test case for get_list

        Get a list's details  # noqa: E501
        """
        pass

    def test_get_lists(self):
        """Test case for get_lists

        Get all the lists  # noqa: E501
        """
        pass

    def test_import_contacts(self):
        """Test case for import_contacts

        Import contacts  # noqa: E501
        """
        pass

    def test_remove_contact_from_list(self):
        """Test case for remove_contact_from_list

        Delete a contact from a list  # noqa: E501
        """
        pass

    def test_request_contact_export(self):
        """Test case for request_contact_export

        Export contacts  # noqa: E501
        """
        pass

    def test_update_attribute(self):
        """Test case for update_attribute

        Update contact attribute  # noqa: E501
        """
        pass

    def test_update_contact(self):
        """Test case for update_contact

        Update a contact  # noqa: E501
        """
        pass

    def test_update_folder(self):
        """Test case for update_folder

        Update a folder  # noqa: E501
        """
        pass

    def test_update_list(self):
        """Test case for update_list

        Update a list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
