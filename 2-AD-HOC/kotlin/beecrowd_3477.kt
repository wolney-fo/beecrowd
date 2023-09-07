import java.util.*
import kotlin.math.*

fun main() {
    val sc = Scanner(System.`in`)
    var x = sc.nextDouble()
    var y = sc.nextDouble()
    var z = sc.nextDouble()
    
    if (x < y + z && y < x + z && z < x + y) {
        val area: Int = (( (y * z) / 2.0 ) + ( 3.0 * (z/2.0).pow(2.0) ) / 2.0).toInt()
        println("AREA = $area")
    }
    else {
        println("Nao eh retangulo!")
    }
}