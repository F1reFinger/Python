import subprocess


def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


if __name__ == '__main__':
    hello_command = "Write-Host 'Hello Wolrd!'"
    hello_info = run(hello_command, cmd)
    if hello_info.returncode != 0:
        print("An error occured: %s", hello_info.stderr)
    else:
        print("Hello command executed successfully!")
    
    print("-------------------------")
    
    bad_syntax_command = "Write-Hst 'Incorrect syntax command!'"
    bad_syntax_info = run(bad_syntax_command)
    if bad_syntax_info.returncode != 0:
        print("An error occured: %s", bad_syntax_info.stderr)
    else:
        print("Bad syntax command executed successfully!")