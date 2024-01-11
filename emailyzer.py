import argparse
from argparse import RawDescriptionHelpFormatter

#introduction
print("------------------------------------------------------------------------------------------")
print("Thank you for using Emailizer by the Dyun\n")
print("To use this tool, you must make sure that your textfile lists names in the following format. (firstname lastname)")
print("Use -h or --help for correct usage and email format options")

print("------------------------------------------------------------------------------------------")

#function for creating custom email formats
def generate_emails(input_file, output_file, domain, option):
    with open(input_file, 'r') as file:
        names = [line.strip().split() for line in file]

    #johndoe@example.com
    if option == 1:
        emails = [f'{first_name.lower()}{last_name.lower()}@{domain}' for first_name, last_name in names]
    #john.doe@example.com
    elif option == 2:
        emails = [f'{first_name.lower()}.{last_name.lower()}@{domain}' for first_name, last_name in names]
    #jdoe@example.com
    elif option == 3:
        emails = [f'{first_name[0].lower()}{last_name.lower()}@{domain}' for first_name, last_name in names]
    #j.doe@example.com
    elif option == 4:
        emails = [f'{first_name[0].lower()}.{last_name.lower()}@{domain}' for first_name, last_name in names]
    #johnd@example.com
    elif option == 5:
        emails = [f'{first_name.lower()}{last_name[0].lower()}@{domain}' for first_name, last_name in names]
    #john.d@example.com
    elif option == 6:
        emails = [f'{first_name.lower()}.{last_name[0].lower()}@{domain}' for first_name, last_name in names]
    #doejohn@example.com
    elif option == 7:
        emails = [f'{last_name.lower()}{first_name.lower()}@{domain}' for first_name, last_name in names]
    #doe.john@example.com
    elif option == 8:
        emails = [f'{last_name.lower()}.{first_name.lower()}@{domain}' for first_name, last_name in names]
    #djohn@example.com
    elif option == 9:
        emails = [f'{last_name[0].lower()}{first_name.lower()}@{domain}' for first_name, last_name in names]
    #d.john@example.com
    elif option == 10:
        emails = [f'{last_name[0].lower()}.{first_name.lower()}@{domain}' for first_name, last_name in names]
    else:
        print("Invalid option selected. Exiting.")
        raise SystemExit(1)

    #write the customized emails to output file
    with open(output_file, 'w') as file:
        file.write('\n'.join(emails))

    #print that the job is done
    print(f'Emails generated and saved to {output_file}')

parser = argparse.ArgumentParser(
    description='Generate emails from a list of names. '
                'Choose an email format option.',
    epilog='''Example:
python3 emailyzer.py -i names.py -o output.txt -d example.com -opt 1
Select one of the options:
1. johndoe@example.com
2. john.doe@example.com
3. jdoe@example.com
4. j.doe@example.com
5. jdoe@example.com
6. j.doe@example.com
7. doejohn@example.com
8. doe.john@example.com
9. djohn@example.com
10. d.john@example.com
''',
    formatter_class=RawDescriptionHelpFormatter
)

#parsing command-line flags & help menu
parser.add_argument('-i', '--input', help='your file containing firstname lastname by line', required=True)
parser.add_argument('-o', '--output', help='name of output file for generated emails', required=True)
parser.add_argument('-d', '--domain', help='target email domain (e.g., gmail.com)', required=True)
parser.add_argument('-opt', '--option', type=int,
                    help='',
                    required=True)
args = parser.parse_args()

generate_emails(args.input, args.output, args.domain, args.option)
