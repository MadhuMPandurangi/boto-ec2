import boto3,time
from exc_sh_cmd import executeShellCmd

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')


#to start instances
def start_instance(ids):
    try:
        response = ec2.instances.filter(InstanceIds = [ids]).start()
        print("\nPlease wait the instance is being started.......\n")
        res = ""
        t1 = time.time()
        while("running"!=res):
            instance = ec2.Instance(ids)
            res = instance.state["Name"]
        t2 = time.time()
        tdelta = str(t2 - t1)   
        print(res)
        print(tdelta+"s is the time taken")
        executeShellCmd(ids)
    except Exception as e:
        print(e)


#to stop instances
def stop_instance(ids):
    try:
        response = ec2.instances.filter(InstanceIds = [ids]).stop()
        print("\nPlease wait the instance is being stopped.......\n")
        res = ""
        t1 = time.time()
        while("stopped"!=res):
            instance = ec2.Instance(ids)
            res = instance.state["Name"]
        t2 = time.time() 
        tdelta = str(t2 - t1)   
        print(res)
        print(tdelta+"s is the time taken")
        
    except Exception as e:
        print(e)        