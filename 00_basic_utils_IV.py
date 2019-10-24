# CONTEXT MANAGERS - they allow to build code with pre and post conditions, executing actions before and after
#					 the actual (main) code runs. They consist of two magic methods: __enter__ and __exit__
#
def start_db():
    pass  # code to start the db


def stop_db():
    pass  # code to stop the db


class DBHandler:
    def __enter__(self):
        """Executed before db_backup static method"""
        start_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Executed after db_backup static method"""
        stop_db()

    @staticmethod
    def db_backup():
        """Main code in the class"""
        pass  # code to make a db backup


with DBHandler():
    DBHandler.db_backup()

# SUBPROCESS MODULE
#
#	- It allows to spawn new processes, connect them to their input/output/error pipes, and obtain their
#       return codes. The recommended approach to invoking subprocess is to use the run() function for
#       all use cases it can handle. For advanced use cases, Popen interface can be used.
#
#   - Function subprocesss.run. Run the command described by args, wait for it to complete and then
#       return a CompletedProcess instance, representing a process that has finished, which contains:
#           · 'args', the args used to launch the process
#           · 'returncode', the exit status of the child process, where 0 indicates success, and a negative
#                           value indicates a signal of termination (POSIX only)
#           · 'stdout' | 'stderr', from the child process. None if not captured, a byte sequence by
#                                  default, or a string if run() was called with 'universal_newlines=True'
#
#   - Function subprocess.Popen. Execute a child program in a new process. It's the underlying layer of
#       run() function, so this last is just a wrapper over Popen, in order to simplify its use.
#

#
# SET operations: intersection, union, symmetric difference, difference, superset...
#
spam = set('spam')
eggs = set('eggs')

print()
print(spam, eggs, sep='\n', end='\n\n')

print(f'spam & eggs: {spam & eggs}')  # AND - intersection (all letters in both words)
print(f'spam | eggs: {spam | eggs}')  # OR - union (all letters in both words)
print(f'spam ^ eggs: {spam ^ eggs}')  # XOR - symmetric difference (all letters in both words, except common ones)
print(f'spam - eggs: {spam - eggs}')  # NOT IN - difference (all letters in first word, not in the second one)
print(f'eggs - spam: {eggs - spam}')
print(f'spam > eggs: {spam > eggs}')  # ALL IN - superset(true if first word contains,
print(f'eggs > spam: {eggs > spam}')  # at least, all letters of second word; false otherwise)
print(f'perfection > perfect: {set("perfection") > set("perfect")}')
