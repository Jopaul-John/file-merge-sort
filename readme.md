### This program is used to test the threads

#### How to run
- To create files run command 
    ```sh
    python3 file-merge.py createfile
    ```
- To merge and sort,
    ```sh
    python3 file-merge.py joinfile
    ```
- After join only one file will be present and hence delete it after use, if run the **createfile** command again, the existing file wont be overwritten and this cause inconsistent data, hence **delete manually**

- To delete all files run command,  
    ```sh
    python3 file-merge.py deletefile
    ```
- To increase the number of file ,open `file-merge.py` and change `NUM_OF_FILES` variable, worked well in 10000 files, but 1 lakh was time confusing
- Not sure of the efficiency :)  
