import java.util.ArrayList;
import java.util.List;

public class Airport {
    private int capacity;
    private List<Plane> availablePlanes = new ArrayList<>();
    private List<Plane> planeInUse = new ArrayList<>();

    public int getCapacity() {
        return capacity;
    }

    public Airport(int capacity) {
        if (capacity <=0){
            throw new IllegalArgumentException();
        }
        else{
            this.capacity = capacity;
        }
    }

    public void ReleasePlane(Plane plane){
        if (planeInUse.contains(plane)){
            availablePlanes.add(plane);
            planeInUse.remove(plane);
        }
        else {
            throw new IllegalArgumentException();
        }
    }

    public Plane AcquireReusable(){
        if(planeInUse.size() == capacity){
            throw new IndexOutOfBoundsException();
        }
        if (availablePlanes.size() == 0){
            availablePlanes.add(new Plane("Samolot"));
        }
        planeInUse.add(availablePlanes.get(0));
        availablePlanes.remove(availablePlanes.get(0));
        return planeInUse.get(planeInUse.size()-1);
    }



}
