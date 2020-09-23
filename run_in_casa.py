####################################################################################################
# execute code in casa
####################################################################################################

# This is wrapped in another try/except because it can easily fail in some old casa versions.

try:
    def run_in_casa(command, cwd=None, keep_cmd_file=False, logfile='casa', interactive=False, pipeline=False, casapath='casa'):
        """Execute CASA commands from within Python.
        Uses the subprocess modul to run CASA in blocking mode. An option to have it run in the background
        will be added in future.

        Parameters
        ----------
        command : str/fstring
            The command(s) to run. Must be a triple quoted string if you want to run multiline
            commands. fstrings can be used to pass parameters from Python to CASA.
        cwd : str
            The directory in which casa is executed. This can be important to set because CASA writes temporary
            images to its current directory. The default is the currect directory, i.e. the directory python
            is in which might not be the directory you want to run casa in.
        keep_cmd_file : bool
            Default: False
            Keep the temporary file that contains the commands to execute.
        logfile : str
            Default: 'casa'
            Filename for the CASA logfile. If 'casa', the CASA default format (casa-XXXXXXXX-XXXXXX.log) is
            used.
        interactive : bool
            Default: False
            Run CASA in interactive mode with the TkAgg backend (MacOS under MacOS) or use the Agg backend.
            Non-interactive (Agg backend) allows to run this in screen or tmux.
        pipeline : bool
            Default: False
            Start the pipeline version of CASA?
        casapath : str
            Default: 'casa'
            Path to the casa executable. By default this points to "casa", i.e. the default CASA
            installation. You might want to point this to e.g. "casa-5.3.0" to start a specific version
            of CASA. In this example "casa-5.3.0" is an alias for the full path at
            "~/programs/casa/casa-5.3.0/bin/casa"

        Please understand this as a poor workaround until CASA 6.0 will run natively in Python3.
        """

        import os
        import numpy as np
        import subprocess
        import shlex

        np.random.seed(None)    # force random numbers if this is called in parallel with a set seed
        commandfile = os.path.join(os.getcwd(), 'casa_cmd.'+str(int(np.random.rand()*1e4))+'.py')
        with open(commandfile, 'w') as f:
            f.write(command)

        # command to execute
        casa_command = casapath+" --nologger --log2term"
        if not logfile=='casa':
            casa_command += " --logfile "+logfile
        if not interactive:
            casa_command += " --agg --nogui"
        casa_command += " -c "+commandfile

        # run casa
        print("\nExecuting CASA:\n\t\x1b[0;31;40m"+casa_command+"\x1b[0m")
        subprocess.call(shlex.split(casa_command), cwd=cwd)

        # keep cmd file?
        if not keep_cmd_file:
            os.system('rm -rf '+commandfile)

except:
    print("\x1b[0;31;40mCould not define run_in_casa().\x1b[0m")


####################################################################################################
#
####################################################################################################
