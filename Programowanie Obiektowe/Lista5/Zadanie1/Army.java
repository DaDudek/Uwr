public class Army implements Comparable<Army>{
    Float getRank()
    {
        return new Float(0);

    }

    public int compareTo(Army military)
    {
        return this.getRank().compareTo(military.getRank());

    }
}