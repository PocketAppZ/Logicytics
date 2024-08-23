from CODE.Custom_Libraries.Log import Log
from CODE.Custom_Libraries.Actions import *


def tasklist():
    try:
        result = subprocess.run(
            "tasklist /v /fo csv",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        with open("tasks.csv", "wb") as file:
            file.write(result.stdout)
        Log(debug=DEBUG).info("Tasklist exported to tasks.csv")
    except subprocess.CalledProcessError as e:
        Log(debug=DEBUG).error(f"Subprocess Error: {e}")
    except Exception as e:
        Log(debug=DEBUG).error(f"Error: {e}")
