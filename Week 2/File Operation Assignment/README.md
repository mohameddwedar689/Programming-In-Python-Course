# Lab: Read in data, store, manipulate and output new data to a file


## There are two objectives of this activity: 
1. Create a function for reading in a file

2. Create a function for writing files.
 <br><br>


## Exercise Instructions:  
<br>

1. Check that the `sampletext.txt` and `file_ops.py` files exist and are present inside the project folder.   
   You can run the `file_ops.py` file by opening a terminal and executing the following command:
    ```
    python3 file_ops.py 
    ```

2. Complete the `read_file()` function to read in the sampletext.txt file using the `open` function and return the entire contents of the file. 

3. Complete the `read_file_into_line()` function so that it returns a data structure of all the contents of the file in a line-by-line sequential order.

4. Fill in the `write_first_line_to_file()` that accepts two arguments. This should write only the first line of the file contents into the given output file.   

    - **Argument 1:** The contents of a file to be written
    - **Argument 2:** The name of an output file.
<br><br>


5. Complete the `read_even_numbered_lines()` to return a list of the even-numbered lines of a file (2, 4, 6, etc.) 

6. Fill in the `read_file_in_reverse()` function to return a list of the lines of a file in reverse order. 

<br>

