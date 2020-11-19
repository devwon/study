import java.util.Arrays;
import java.util.List;

public class Java8Test{
    public static void main(String[] args){
        final List<Integer> numbers = Arrays.asList(1,2,3,4,5,6,7,8);
        
        System.out.println("Filtered Map:" +
            numbers.stream()
                .filter(number -> number > 3)
                .filter(number -> number < 9)
                .map(number -> number * 2)
                .filter(number -> number > 10)
                .findFirst().get()
        );
        
        String[] array = {"Won e", "Kang e", "Park e"};

        // map
        Stream<String> arrayStream = Stream.of(array);
        arrayStream.map(e -> e.toUpperCase())
        .forEach(e -> System.out.println(e));
        
        // flatmap
        Stream<String> arrayStream2 = Stream.of(array);
        arrayStream2
        .map(e -> e.split("\\s+"))
        .flatMap(Arrays::stream)
        .distinct()
        .forEach(System.out::println);
    }
}
