import sys
## Write Caution
WARNING="""

#####################################################################################
#                                                                                     #
# This is a simple script which can download and upload blogs from and to Medium      #
# This script is provided without any gurantee                                        #
# Please ensure you own the rights to download or upload the blog you are downloading #
# This Tool cannont gurantee the ownership/permission to download content             #
# It is your responsibility to ensure you have the necessary permissions before       #
# downloading any content. This tool cannot validate your ownership claims.           #
# Tool Functionality: This tool is provided "as is" with no guarantee of functionality#
# or success. Downloading content may not work as expected or may not be compatible   #
# with your system.                                                                   #
#                                                                                     #
# Before proceeding, please make sure:                                                #
#                                                                                     #
#     Do you own the rights to all the content you are downloading?(y/n)              #
#     Are you authorized to download this content by the copyright holder?(y/n)       #
#                                                                                     #
#                                                                                     #
#######################################################################################
"""
def Caution():
    print(WARNING)
    y_n=input("Type \"y\" and press Enter to proceed, or type \"n\" and press Enter to cancel.: ")
    if y_n=="y":
        return
    sys.exit()