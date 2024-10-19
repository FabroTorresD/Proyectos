package utn.frc.bda.repositories;

import jakarta.persistence.EntityManager;
import utn.frc.bda.entities.Repository;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collection;

public class RepositoryRepository {

    private EntityManager em;

    public RepositoryRepository(EntityManager entityManager){
        this.em = entityManager;
    }

    public void saveAll(Collection<Repository> repositoriesToSave){
        repositoriesToSave.forEach(this::save);
    }

    public void save(Repository repository){
        begin();
        em.persist(repository);
        commit();
    }

    public void createDB(String sqlFilePath) throws IOException {
        begin();
        String script = Files.readString(Paths.get(sqlFilePath));

        em.createNativeQuery(script).executeUpdate();
        commit();
    }


    private void begin() {
        em.getTransaction().begin();
    }

    private void commit() {
        em.getTransaction().commit();
    }

}
