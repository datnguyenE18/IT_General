- **Application = Service**
</br>

- **Script:** simply a file, which contains a set of normal linux commands that the command shell will perform automatically in the given order
</br>

- **Process:**
  - Whenever you enter a command at the shell prompt, it invokes a program
  - While this program is running it is called a process
  - Every process in a LINUX system has a unique PID - process id
  - Login shell is also a process, created for us upon logging in and existing until we logout.
  - Process id: every process in a LINUX system has a unique PID - process identifier
</br>

- **Daemon:**
  - a long-running background process that answers requests for services
  - also a process, but it keeps on running the background and it keeps listening to the incoming traffic or outgoing traffic.
  - runs unobtrusively in the background, rather than under the direct control of a user, waiting to be activated by the occurance of a specific event or condition.
</br>

- **Threads:**
  - every process could have multiple threads associated with it.
  - Service --> Process --> thread1, thread2,…
</br>

- **Job** or **Workorder** = Run a service or process at a shedule time
