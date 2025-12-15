import java.util.Arrays;
class Solution {
    public double solution(int[] numbers) {
        double answer = Arrays.stream(numbers).sum() / (float)numbers.length;
        return answer;
    }
}