
filename = "%s_hourly.csv" % dataset   
with open(filename, 'ab') as csvfile:
    linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    linewriter.writerow(["PATIENT_ID","LABEL","ACCELERATION","X.PSD.LOW","X.PSD.LOWMID",'X.PSD.MIDHIGH','X.PSD.HIGH','Y.PSD.LOW','Y.PSD.LOWMID','Y.PSD.MIDHIGH','Y.PSD.HIGH','Z.PSD.LOW','Z.PSD.LOWMID','Z.PSD.MIDHIGH','Z.PSD.HIGH','TIME']) 