import boto3,datetime,pprint

region = "ap-south-1c"
ec2 = boto3.resource('ec2')

def create_Snapshot(ids):
    date = str(datetime.datetime.now().strftime('%d-%b-%y/%H:%M:%S'))
    instance_id=ids
    name = "Snapshot is of InstanceID: "+instance_id+" / Created on "+date
    print(name)

    instance = ec2.Instance(instance_id)
    volumes = instance.volumes.all()
    print("list of volumes are:")
    for v in volumes:
        print(v.id)
    volume_id = raw_input("Please choose and type the volumes listed above and press enter:")   
    try: 
        snapshot = ec2.create_snapshot(VolumeId=volume_id, Description=name)
        pprint.pprint(snapshot)
    except Exception as e:
        print('error', e)  
