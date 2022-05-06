# ------------------------------------------------------------
# This is the main compiler that takes in .ts files as inputs and runs the game.
# ------------------------------------------------------------
import argparse
import io
import pprint

from helpers import validate_extensions
from lexer import TetroScriptLexer
from parser import TetroScriptParser
# Command line arguments parser
from translator import TetroScriptTranslator

argparser = argparse.ArgumentParser()
argparser.add_argument('files', nargs='+', help='TetroScript files to compile and run.')
args = argparser.parse_args()

# .tsc file path
filepaths = args.files

# Validate if file extension is .tsc
if not validate_extensions(filepaths):
    print("ERROR: Only .ts files are supported")
    exit(-1)

# Combine all files
buffer = io.StringIO()
for filepath in filepaths:
    with open(filepath, "rt") as f:
        buffer.write(f.read())
buffer.seek(0)

lexer = TetroScriptLexer()
parser = TetroScriptParser()
translator = TetroScriptTranslator()

game_sequence, game_config = translator.translate(*parser.parse(lexer.tokenize(buffer.read())))

# TODO Run game using game config
for game in game_sequence:
    print("Play Game:", game)
    print("Game Config:")
    pprint.pprint(game_config[game])
