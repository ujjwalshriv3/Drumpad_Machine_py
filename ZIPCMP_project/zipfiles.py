from types import NoneType
import zipfile # import the zipfile module to compress the file
import sys # import the sys module to get the command line arguments
import os # import the os module to get the path of the directory to be zipped and the name of the directory to be zipped


# compress file function to compress the file and store it in the same directory as the file
def zip_file(file_path): # file_path is the path of the file to be zipped
    compress_file = zipfile.ZipFile(file_path + '.zip', 'w') # w for write and r for read
    compress_file.write(path, compress_type=zipfile.ZIP_DEFLATED) # ZIP_DEFLATED for compression and ZIP_STORED for no compression
    compress_file.close() # close the file and return the zip file path


# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dir_name): # dir_name is the path of the directory to be zipped
    # setup file paths variable to store all the file paths
    file_paths = [] # list of all the file paths

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dir_name): # os.walk() is a generator that returns a tuple of 3 values which are the path of the directory, the directories in the directory and the files in the directory
        for filename in files: # iterate over the files and add them to the list
            # Create the full file path by using os module and join function.
            file_path = os.path.join(root, filename) # os.path.join() joins the path of the directory and the file name to create the full file path of the file and store it in the file_path variable
            file_paths.append(file_path) # append the file path to the list of file paths to be zipped
            

    # return all paths of the directory to be zipped by using the list of file paths by using the zip_dir function
    return file_paths


def zip_dir(dir_path, file_paths): # dir_path is the path of the directory to be zipped and file_paths is the list of all the file paths in the directory to be zipped
    # write files and folders to a zipfile
    compress_dir = zipfile.ZipFile(dir_path + '.zip', 'w') # Compress_dir is the zipfile object which stores the zip file and w for write and r for read
    with compress_dir: # with statement to open the zip file and close it automatically called context manager
        # write each file separately
        for file in file_paths: # iterate over the list of file paths
            compress_dir.write(file) # write the file to the zip file using the write function of the zipfile object

def scrtoprgswitcher(): # this function is used to switch between the script and the program
    dir_list = [] # list of all the directories to be zipped
    nofiles = int(input("Enter the number of files to be zipped: ")) # number of files to be zipped
    for i in range(nofiles): # iterate over the number of files to be zipped
        dir_list.append(input("Enter the path of the directory to be zipped: ")) # append the path of the directory to be zipped to the list of directories to be zipped
    return dir_list # return the list of directories to be zipped

def pathlistdecoder():
    listedpath = scrtoprgswitcher() # call the scrtoprgswitcher function to get the list of directories to be zipped
    print(listedpath)
    for i in listedpath: # iterate over the list of directories to be zipped
        print(i)
        # path = i # function problem not working
        
if __name__ == "__main__": # main function to run the program which is the entry point of the program and is executed first
    # if __name__ == "__main__" is used to check if the file is being run directly or imported from another file and if it is being run directly then the code inside the if statement is executed and if it is being imported from another file then the code inside the if statement is not executed
    # here is no main function in python so we use the if __name__ == "__main__" statement to run the program and the code inside the if statement is executed first
    # Declare the name of the directory to be zipped, path
    path = sys.argv[1] # get the path of the file to be zipped from the command line arguments using the sys module and store it in the path variable
        
    if os.path.isdir(path): # check if the path is a directory using the os module and the isdir function
        files_path = retrieve_file_paths(path) # get the list of all the file paths in the directory to be zipped using the retrieve_file_paths function and store it in the files_path variable 
        print('The following list of files will be zipped:', files_path) # print the list of files to be zipped to the user
        for file_name in files_path: # iterate over the list of file paths to be zipped
            print(file_name) # print the file name to be zipped to the user before zipping it
        zip_dir(path, files_path) # zip the directory using the zip_dir function and pass the path of the directory to be zipped and the list of file paths to be zipped
    elif os.path.isfile(path): # check if the path is a file using the os module and the isfile function
        print('The %s will be zipped:' % path) # here %s is the placeholder for the path of the file to be zipped and % is the operator to concatenate the string and the path of the file to be zipped
        zip_file(path) # zip the file using the zip_file function and pass the path of the file to be zipped
    else: # if the path is neither a file nor a directory then print the following message
        print('a special file(socket,FIFO,device file), please input file or dir')