package utn.frc.bda;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import utn.frc.bda.services.RepositoryService;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("H2_PERSISTENCE");
        EntityManager em = emf.createEntityManager();

        RepositoryService repositoryService = new RepositoryService(em);
        // Punto 1 y 2
        repositoryService.loadRepositoriesFromFile();

        // Punto 3
        System.out.println("Total repositorios importados: " + repositoryService.getCantRepositories());
        System.out.println("Total estrellas: " + repositoryService.getTotalStars());

        // Punto 4
        repositoryService.genreLanguageFile();

        // Punto 5
        repositoryService.printUsersWithRepoAndStars();

        // Punto 6
        repositoryService.saveRepositoriesToDB();

        emf.close();
        em.close();
    }
}