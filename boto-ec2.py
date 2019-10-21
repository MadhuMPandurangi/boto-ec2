import boto3, json, pprint, time
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')


#to list instances
def list_instances():
    for instance in ec2.instances.all():
       print (instance.id)


#tostart instances
def start_instance(ids):
    inst = [ids]
    response = ec2.instances.filter(InstanceIds = inst).start()
    print("\nPlease wait the instance is being started.......\n")
    res = ""
    while("running"!=res):
        response = client.describe_instance_status(InstanceIds = [ids], IncludeAllInstances=True)
        res = response['InstanceStatuses'][0]['InstanceState']['Name']
    print(res)


#to stop instances
def stop_instance(ids):
    inst = [ids]
    response = ec2.instances.filter(InstanceIds = inst).stop()
    print("\nPlease wait the instance is being stopped.......\n")
    res = ""
    while("stopped"!=res):
        response = client.describe_instance_status(InstanceIds = [ids], IncludeAllInstances=True)
        res = response['InstanceStatuses'][0]['InstanceState']['Name']
    print(res)
    


#to check the status of instance
def status_check(ids):
    inst = [ids]
    response = (client.describe_instance_status(InstanceIds = [ids], IncludeAllInstances=True))
    #pprint.pprint(response)
    print(response['InstanceStatuses'][0]['InstanceState']['Name'])




def main():
    while(1):
        print("1. List Instances\n2. Start\n3. Stop\n4. Status")
        val = input("Enter your option of the above mentioned operation: ")
        if(val==1):
            list_instances()

        if(val==2):
            ids = raw_input("Enter the instance ID: ")
            start_instance(ids)

        if(val==3):
            ids = raw_input("Enter the instance ID: ")
            stop_instance(ids)

        if(val==4):
            ids = raw_input("Enter the instance ID: ")
            status_check(ids)    


        flag = (raw_input("If you want to continue(y/n): "))
        if(flag=="n"):
            break            
        


    if __name__== "__main__" :
        return 0

main()