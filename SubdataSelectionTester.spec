/*
A KBase module: SubdataSelectionTester
*/

module SubdataSelectionTester {

    typedef structure {
        string ref;
        list<string> included;
    } SubObjectIdentity;

    typedef structure {
        UnspecifiedObject data;
    } ObjectData;

    funcdef get_object_subset(list<SubObjectIdentity> sub_object_ids)
        returns (list<ObjectData> data) authentication required;

    funcdef hello_world(string name) returns (string message) 
        authentication required;
};
