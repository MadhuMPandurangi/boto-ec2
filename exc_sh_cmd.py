import boto.ec2
from boto.manage.cmdshell import sshclient_from_instance

REGION = 'ap-south-1'
PATH_TO_KEYPAIR = '/home/madhu/Desktop/AWS/MMP-key-pair.pem'
USER_NAME = 'ubuntu'
CMD = "sudo systemctl stop couchdb && cd /home/ubuntu/app && sudo docker-compose up"


def executeShellCmd(ids):
    print(type(ids))
    try:
        # Connect to your region of choice
        conn = boto.ec2.connect_to_region(REGION)
        # Find the instance object related to my instanceId
        instance = conn.get_all_instances([ids])[0].instances[0]
        print(instance)
        # Create an SSH client for our instance
        #    key_path is the path to the SSH private key associated with instance
        #    user_name is the user to login as on the instance (e.g. ubuntu, ec2-user, etc.)
        ssh_client = sshclient_from_instance(instance,
                                            PATH_TO_KEYPAIR,
                                            user_name=USER_NAME)
        print(ssh_client)
        # Run the command. Returns a tuple consisting of:
        #    The integer status of the command
        #    A string containing the output of the command
        #    A string containing the stderr output of the command
        status, stdout, stderr = ssh_client.run(CMD)
        print("status: ",status)
    except Exception as e:
        print(e)    
