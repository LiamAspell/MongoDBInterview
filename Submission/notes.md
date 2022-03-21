This provides some information regarding the solution: 

    Task 1 - Add a 'Total' line to the receipt
    --------------------------------------------------------------------------------------------------------------------------------------------------------------
        Adding a 'Total' Line to the Receipt 
            Implemented this in print_receipt method, where the price value of each value pair is added together and printed at the end. 

    Task 2 - Make the receipt print items in the order that they were scanned
    --------------------------------------------------------------------------------------------------------------------------------------------------------------
        Make the receipt print items in the order that they were scanned
            Again this is implemented in the print_receipt method, added an extra object value to read the key value pairs into a list, and outputted those pairs
            using an incremental loop to ensure the print_receipt method followed desired structure. 

    Task 3 - Adding support for different formats in print_receipt 
    --------------------------------------------------------------------------------------------------------------------------------------------------------------
    	Passing a value through the print_receipt method which represents the format of the contents when printed to receipt
            Value = 1  - The items print in the form {Item} - {Quantity} - {Price}
            Value = 2  - The items print in the form {Price} - {Quantity} - {Item}
            Of course, there is scope to expand this using this method, whereby passing a value of 3, 4, 5 and so on would be representative of other formats also 

    Task 4 - Extend coverage of the Test Suite
    --------------------------------------------------------------------------------------------------------------------------------------------------------------
        Updated the test suite to include testing of new features that I added functionality for as part of the Assigment:
            Task 1      -       def test_on_totals_1()
                                def test_on_totals_2()
                                def test_on_totals_3()
            
            Task 2      -       def test_on_each_individual_item_scanned_1()
                                def test_on_each_individual_item_scanned_2()
            
            Task 3      -       def test_on_regular_format() 
                                def test_on_alternative_format() 

            

    