import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser("vortexasdk")
    parser.add_argument('check-setup', help='Run a series of tests to check that the vortexasdk is setup correctly.')
    args = parser.parse_args()

    if 'check-setup' in args:
        from vortexasdk.check_setup import run_all_checks

        run_all_checks()
