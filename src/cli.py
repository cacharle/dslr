class CommandLineInterface:
    def __init__(self):
        pass

    def parse_args(self):
        parse = argparse.ArgumentParser(prog="dslr_cli",
                                        description="CLI for the dslr project")
        subparser = parser.add_subparsers(dest="subparser_name")
        parser_describe = subparsers.add_parser("describe",
                                                help="give useful information about a dataset")
        parser_describe.add_argument("path", help="path to the dataset")
        parser_describe.set_defaults(func=self._describe)

        self.args = parser.parse_args(sys.argv[1:])

    def exec_args(self):
        if self.args.subparser_name is None:
            print("{} --help for more information".format(sys.argv[0]))
            return
        self.args.func()

    def _describe(self):
        describe.describe(self.args.path)


if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.parse_args()
    cli.exec_args()
