import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)
    val PI = 3.14159
    val raio: Double = sc.nextDouble()

    println("%.4f".format(PI * (raio * raio)))
}