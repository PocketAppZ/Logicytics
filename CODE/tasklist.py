from __lib_class import *

if __name__ == "__main__":
    log = Log(debug=DEBUG)


def tasklist():
    """
    Retrieves a list of running tasks on the system and exports the result to a CSV file.

    Parameters:
    None

    Returns:
    None
    """
    try:
        result = subprocess.run(
            "tasklist /v /fo csv",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        with open("tasks.csv", "wb") as file:
            file.write(result.stdout)
        log.info("Tasklist exported to tasks.csv")
    except subprocess.CalledProcessError as e:
        log.error(f"Subprocess Error: {e}")
    except Exception as e:
        log.error(f"Error: {e}")


tasklist()
