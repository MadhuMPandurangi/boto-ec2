import boto3, json, pprint, time, datetime
from snapShot import create_Snapshot
from start_stopInstance import start_instance
from start_stopInstance import stop_instance
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')


#to list instances
def list_instances():
    try:
        for instance in ec2.instances.all():
            print(instance.id)
    except Exception as e:
        print(e)   
    


#to check the status of instance
def status_check(ids):
    try:
        instance = ec2.Instance(ids)
        print(instance.state["Name"])
    except Exception as e:
        print(e)    

def reboot_instance(ids):
    try:
        response = client.reboot_instances(InstanceIds=[ids], DryRun=False)
        print('Success')
    except Exception as e:
        print('Error:', e)


def list_volumes(ids):
    instance = ec2.Instance(ids)
    volumes = instance.volumes.all()
    print("list of volumes are:")
    for v in volumes:
        print(v.id)



def main():
    while(1):
        print("1. List Instances\n2. Start\n3. Stop\n4. Status\n5. Reboot Instance\n6. List Volumes\n7. Create Snapshot")
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

        if(val==5):
            ids = raw_input("Enter the instance ID: ")
            reboot_instance(ids)  

        if (val==6):
            ids = raw_input("Enter the instance ID: ")
            list_volumes(ids)    

        if(val==7):
            ids = raw_input("Enter instance ID. Press 1 and enter to get the list of Instances: ")
            if(ids == '1'):
               list_instances()
            else:
                create_Snapshot(ids)


        flag = (raw_input("If you want to continue(y/n): "))
        if(flag=="n"):
            break            
        


    if __name__== "__main__" :
        return 0

main()