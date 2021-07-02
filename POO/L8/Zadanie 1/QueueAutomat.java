import java.util.LinkedList;
import java.util.Queue;


public class QueueAutomat {
    private Queue<Command> commandQueue = new LinkedList<>();
    private Thread t1 ;
    private Thread t2 ;
    private Thread t3 ;

    public QueueAutomat() throws InterruptedException {
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                try {
                    updateQueue();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        Runnable runnable1 = new Runnable() {
            @Override
            public void run() {
                try {
                    executeCommand();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };

        t1 = new Thread(runnable);
        t2 = new Thread(runnable1);
        t3 = new Thread(runnable1);

        t1.start();
        t2.start();
        t3.start();

    }

    private void addRandomCommand(){
        int min = 0;
        int max = 3;
        int random_int = (int)Math.floor(Math.random()*(max-min+1)+min);
        Commands[] commands = Commands.values();
        switch (commands[random_int]) {
            case FTP -> this.commandQueue.offer(new FTPCommand("przykładowy url ftp", "plik1.txt"));
            case HTTP -> this.commandQueue.offer(new HTTPCommand("przykładowy url ftp", "plik1.txt"));
            case COPY_FILE -> this.commandQueue.offer(new CopyFileCommand("plik1.txt", "plik2.txt"));
            case CREATE_FILE -> this.commandQueue.offer(new CreateFileCommand("plik1.txt"));
        }
    }

    private  void executeCommand() throws InterruptedException {
        while (true){
            if (commandQueue.size() > 0){
                Command actuallCommand = this.commandQueue.poll();
                if (actuallCommand != null){
                    actuallCommand.Execute();
                }
            }
            Thread.sleep(1000);
        }
    }

    private void updateQueue() throws InterruptedException {
        while(true){
            addRandomCommand();
            Thread.sleep(500);
        }
    }

}