import sys;
import os;
sys.path.insert(0,os.getcwd()+"/"+"Viruses");

import VirusProgram;
import DVirus;
import RVirus;


viruses=[];
#Create some new viruses for students to look for.
viruses.append(VirusProgram.Virus("B_VirusDirectory",100,100,0));
viruses.append(VirusProgram.Virus("G_VirusDirectory",100,100,1));
viruses.append(DVirus.DVirus("D_VirusDirectory",100,100,0));
viruses.append(DVirus.DVirus("DA_VirusDirectory",100,100,1));
viruses.append(DVirus.DVirus("DH_VirusDirectory",100,100,2));
viruses.append(DVirus.DVirus("DHSH_VirusDirectory",100,100,3));
viruses.append(DVirus.DVirus("DASH_VirusDirectory",100,100,4));
viruses.append(RVirus.RVirus("R_VirusDirectory",100,100,0));
for virus in viruses:
    #Actually "initialize" each type of virus.
    virus.CreateVirus();
print("All virus files have been created. Good luck!");
