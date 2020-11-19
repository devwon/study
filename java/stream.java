import java.util.Arrays;
import java.util.stream.Stream;
import java.util.Iterator;

public class Java8Test{
    public static void main(String[] args){
        
        // Stream
        // before java 8
        // *Iterator 이용
        System.out.println("Before Java 8");
        List<String> list1 = Arrays.asList("데브원", "원데브", "깃허브");
        Iterator<String> iterator = list1.iterator();
        while(iterator.hasNext()){
            String name = iterator.next();
            System.out.println(name);
        }
        
        // after java 8
        // *Stream 이용
        System.out.println("After Java 8");
        List<String> list2 = Arrays.asList("데브원", "원데브", "깃허브");
        Stream<String> stream = list2.stream();
        stream.forEach(name -> System.out.println(name));
    }
}
