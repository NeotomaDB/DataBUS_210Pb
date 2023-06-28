import argparse
import os
def parseArguments():
    """_Parse commandline arguments to the Uploader_
       
       Args:
            none
        Returns:
            _dict_: A dict object with two parameters, 'data' and 'yml',
                    indicating the location of the data files to be used,
                    and the yaml document used for validation.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--data',
                        type = str,
                        nargs = '?',
                        const = 'data/',
                        default = 'data/',
                        help = 'Path to the data directory')
    parser.add_argument('--template',
                        type = str,
                        nargs = '?',
                        const = 'template.yml',
                        default = 'template.yml',
                        help = 'YAML Template file to use for validation')

    args = parser.parse_args()

    if not os.path.isdir(args.data):
        raise FileNotFoundError("There is no directory named '" +
                                args.data +
                                "' within the current path. Please set the --data property.")

    if not os.path.isfile(args.template):
        raise FileNotFoundError("The file '" +
                                args.template +
                                "' could not be found within the current path." +
                                " Please set the --template property.")

    return {'data': args.data, 'yml': args.template}