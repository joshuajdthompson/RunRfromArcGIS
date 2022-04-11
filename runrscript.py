'''
4/11/2022 - Josh Thompson (joshuajamesdavidthompson@gmail.com)

For Run R Script from ArcGIS Pro.

User provides path to R exe, and the script they want to run, 

'''

import arcpy
import subprocess as sub
import os


class RunRScript(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Run R Script From ArcGIS"
        self.description = "Runs and R Script from ArcGIS"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        
        #params[0]
        rbinfolder = arcpy.Parameter(
            datatype = "DEFolder",
            name = 'rbinfolder',
            displayName = 'Folder that contains R Executable',
            parameterType = 'Required',
            direction = 'Input')

        #params[1]
        rscript = arcpy.Parameter(
            datatype = "DEFile",
            name = 'rscript',
            displayName = 'R Script',
            parameterType = 'Required',
            direction = 'Input')
        
        params = [rbinfolder,
                  rscript]
        
        return params

    def isLicensed(self):

        return True

    def execute(self, parameters, messages):
    
        #get parameters
        rbinfolder = parameters[0].valueAsText
        arcpy.AddMessage('--Folder Containing Rscript.exe: {}'.format(rbinfolder))
        rscript = parameters[1].valueAsText
        arcpy.AddMessage('--Folder Containing R Script: {}'.format(rscript))
        command = os.path.join(rbinfolder,r"Rscript.exe")
        arcpy.AddMessage('--Full Path: {}'.format(command))
        path2script =  rscript
        cmd_line = [command, path2script]
        sub.Popen(cmd_line)
        return
