import java.util.Scanner;

//Alunos: João Alba, Nicole Taufenbach

public class CercaFerroviaria {

    private static Scanner sc;

    public static void main(String[] args) {
        while (true) {
            sc = new Scanner(System.in);

            System.out.println("Digite 1 para cifrar ou 2 para decifrar");
            boolean isCifrar = sc.nextInt() == 1;
            System.out.println("Informe a quantidade de trilhos");
            int qtdTrilhos = sc.nextInt();
            sc.nextLine();
            if (isCifrar) {
                cifrar(qtdTrilhos);
            } else {
                decifrar(qtdTrilhos);
            }
        }
    }

    private static void cifrar(int qtdTrilhos){
        System.out.println("Informe a frase: ");
        String frase = sc.nextLine().replace(" ", "");

        char[][] matriz = createMatriz(qtdTrilhos, frase);

        StringBuilder builder = new StringBuilder();
        for (char[] chars : matriz) {
            for (char letra : chars) {
                if (letra != Character.MIN_VALUE) {
                    builder.append(letra);
                }
            }
        }

        System.out.println("Frase cifrada: " + builder);
    }

    private static void decifrar(int qtdTrilhos){
        System.out.println("Informe a frase: ");
        String frase = sc.nextLine().replace(" ", "");
        String placeholder = "@".repeat(frase.length());
        char[][] matrizPlaceholder = createMatriz(3, placeholder);

        int contador = 0;
        for (int i = 0; i < matrizPlaceholder.length; i++) {
            for (int j = 0; j < matrizPlaceholder[i].length; j++) {
                if (matrizPlaceholder[i][j] == '@') {
                    matrizPlaceholder[i][j] = frase.toCharArray()[contador];
                    contador++;
                }
            }
        }

        StringBuilder builder = new StringBuilder();
        boolean descendo = true;
        int contadorVert = -1;
        for(int i = 0; i < frase.length(); i++){
            if(contadorVert+1 == qtdTrilhos){
                descendo = false;
            }

            if(contadorVert == 0){
                descendo = true;
            }

            if(descendo){
                contadorVert++;
            }else{
                contadorVert--;
            }

            builder.append(matrizPlaceholder[contadorVert][i]);
        }

        System.out.println("Frase decifrada: " + builder);
    }

    private static char[][] createMatriz(int qtdTrilhos, String frase){
        char[][] matriz = new char[qtdTrilhos][frase.length()];

        boolean descendo = true;
        int contadorVert = -1;
        for(int i = 0; i < frase.length(); i++){
            if(contadorVert+1 == qtdTrilhos){
                descendo = false;
            }

            if(contadorVert == 0){
                descendo = true;
            }

            if(descendo){
                contadorVert++;
            }else{
                contadorVert--;
            }

            matriz[contadorVert][i] = frase.toCharArray()[i];
        }

        return matriz;
    }
}
