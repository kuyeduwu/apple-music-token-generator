import sys, getopt
import time, datetime, calendar
import jwt

def printHelp():
    with open("help", "r") as f:
        for line in f:
            print(line)

def generate(secret, keyId, teamId, expDays, algorithm="ES256"):
    time_now = int(time.time())
    time_exp = int(calendar.timegm((datetime.datetime.now() + datetime.timedelta(days=expDays)).utctimetuple()))

    headers = {
        "alg": "ES256",
        "kid": algorithm
    }

    payload = {
        "iss": teamId,
        "iat": time_now,
        "exp": time_exp
    }

    token = jwt.encode(payload, secret, algorithm=algorithm, headers=headers)

    return token

def main(args):

    keySecret = ""      # the secret in the .p8 key file downloaded from apple
    keyId = ""          # the 10-character key id
    teamId = ""         # the apple developer account team id
    expireAfter = 1     # the expire time, default one day after

    try:
        opts, args = getopt.getopt(args, "hf:k:t:e:", ["help", "file=", "key=", "team=", "expire="])
    except getopt.GetoptError as ex:
        print(ex)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ["-h", "--help"]:         # help
            printHelp()
            sys.exit()

        elif opt in ["-f", "--file"]:       # secret
            with open(arg, "r") as f:
                keySecret = f.read()

        elif opt in ["-k", "--key"]:        # key
            keyId = arg

        elif opt in ["-t", "--team"]:       # team
            teamId = arg

        elif opt in ["-e", "--expire"]:     # expire
            if int(arg) > 180:
                print("The maximum allowed value for -e is 180.")
                sys.exit(2)
            expireAfter = int(arg)

    if keySecret == "" or keyId == "" or teamId == "":
        print("Missing mandatory argument(s).")
        printHelp()
        sys.exit(2)

    print(generate("", keyId, teamId, expireAfter))
    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])