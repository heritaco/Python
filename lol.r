# Instala ggplot2 si aún no lo has hecho
# install.packages("ggplot2")

# Carga la biblioteca
library(ggplot2)

# Define la función paramétrica para la curva
parametric_curve <- function(t) {
  x <- (t - 1) * 0 + t * 4
  y <- (t - 1) * 1 + t * 0
  return(data.frame(x = x, y = y))
}

# Genera datos para la curva con t en el intervalo [0, 1]
curve_data <- lapply(seq(0, 1, 0.01), parametric_curve)
curve_data <- do.call(rbind, curve_data)

# Grafica la curva
ggplot(curve_data, aes(x, y)) +
  geom_path() +
  labs(title = "Curva paramétrica",
       x = "X",
       y = "Y") +
  theme_minimal()

