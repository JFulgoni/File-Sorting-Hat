__author__ = 'johnfulgoni'

import shutil
import os
from file_management import file_helper

SUPPORTED_FILETYPES = ['pdf']
BOLD = '\033[1m'
END_BOLD = '\033[0m'

def determine_path(result):
    #TODO Implement smart analysis of words here
    # from here, you can do a smart analysis using nearest neighbor
    # or just base it on if then
    return "Data/Results/"

def move_file(source, destination):
    if(prompt_move(source, destination)):
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.move(source, destination)
        print "Successfully moved to " + destination
    else:
        print source + " was not moved."

def prompt_move(source, destination, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    question = "Move " + source + " to " + destination + "?"
    while True:
        print question + prompt
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print "Please respond with 'yes' or 'no' (or 'y' or 'n').\n"

def start_prompt(source):
    print "Starting the File Sorting Hat!"
    print "Currently supporting the following file types:"
    print "Operating on file: " + source
    print "..."

def end_prompt():
    print "Thank you for using the File Sorting Hat!"

if __name__ == '__main__':
    #source_file = sys.argv[1]
    source_file = 'Data/SampleFinal.pdf'
    start_prompt(source_file)
    filename = source_file.split('/')[-1]
    extension = filename.split('.')[-1]

    if extension not in SUPPORTED_FILETYPES:
        print "File extension " + BOLD + extension + END_BOLD + " not supported at this time"
        exit()

    result = ''
    if 'pdf' == extension:
        result = file_helper.parse_pdf(source_file)
        #print pdf_result
    if result:
        destination_file = determine_path(result) #+ filename
        move_file(source_file, destination_file)
    else:
        print "No data returned from parse. No action taken."
    end_prompt()