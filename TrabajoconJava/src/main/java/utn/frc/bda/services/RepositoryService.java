package utn.frc.bda.services;

import jakarta.persistence.EntityManager;
import utn.frc.bda.entities.Language;
import utn.frc.bda.entities.Repository;
import utn.frc.bda.entities.Tag;
import utn.frc.bda.entities.User;
import utn.frc.bda.repositories.RepositoryRepository;

import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.String.format;

public class RepositoryService {

    private static final String REPOSITORY_FILE_PATH = System.getProperty("user.dir") + "/src/main/resources/repositories/repositories.txt";
    private static final String DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'";
    private static final String LANGUAGE_FILE_PATH = System.getProperty("user.dir") + "/src/main/resources/languages/languages.txt";
    private static final String SQL_FILE_PATH = System.getProperty("user.dir") + "/src/main/resources/repositories/init-bd.sql";

    private RepositoryRepository repositoryRepository;

    private TagService tagService;
    private UserService userService;
    private LanguageService languageService;

    private Map<Long, Repository> repositoriesMap;

    public RepositoryService(EntityManager em) {
        repositoriesMap = new HashMap<>();
        tagService = new TagService();
        userService = new UserService();
        languageService = new LanguageService();
        repositoryRepository = new RepositoryRepository(em);
    }

    public void loadRepositoriesFromFile() {
        File file = new File(REPOSITORY_FILE_PATH);
        try {
            Scanner sc = new Scanner(file);
            // Salteamos primera linea
            sc.nextLine();

            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                Repository repository = lineToRepository(line);
                repositoriesMap.put(repository.getId(), repository);
            }
        } catch (FileNotFoundException | ParseException e) {
            throw new RuntimeException(e);
        }
    }


    private Repository lineToRepository(String line) throws ParseException {
        String delim = "\\|";
        String[] parts = line.split(delim);

        // REPOSITORY_ID|USER_NAME|REPOSITORY_NAME|DESCRIPTION|LAST_UPDATE|LANGUAGE|STARS|TAGS|URL
        Long repositoryId = Long.valueOf(parts[0]);
        String userName = parts[1];
        User user = userService.getOrCreateUser(userName);

        String repositoryName = parts[2];
        String description = parts[3];
        Date lastUpdate = new SimpleDateFormat(DATE_FORMAT).parse(parts[4]);

        String languagesNames = parts[5];
        Set<Language> languages = languageService.getOrCreateLanguage(languagesNames);

        Double stars = Double.valueOf(parts[6]);

        String tagsNames = parts[7];
        Set<Tag> tags = tagService.getOrCreateTag(tagsNames);

        String url = parts[8];

        return new Repository(repositoryId, repositoryName, description, lastUpdate, stars, url, user, tags, languages);

    }

    public int getCantRepositories() {
        return repositoriesMap.size();
    }

    public Double getTotalStars() {
        Double totalStars = 0.0;

        for (Repository repository : repositoriesMap.values()) {
            totalStars += repository.getStars();
        }

        return totalStars;
    }

    public void genreLanguageFile() {
        File file = new File(LANGUAGE_FILE_PATH);

        Set<Language> languages = new HashSet<>();

        for (Repository repository : repositoriesMap.values()){
            for (Language language : repository.getLanguages()){
                languages.add(language);
            }
        }

        try(FileWriter writer = new FileWriter(file)){
            writer.append("Lenguaje, Cantidad Repositorios, Suma de estrellas\n");

            for (Language language : languages){
                writer.append(format("%s,%s,%s",
                        language.getName().isEmpty() ? "Sin Lenguaje" : language.getName(),
                        language.numberOfRepositories(),
                        language.numberOfStars()));
                writer.append("\n");
            }

            writer.flush();
            System.out.println("Archivo Texto creado correctamente: " + LANGUAGE_FILE_PATH + "\n");

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void printUsersWithRepoAndStars(){
        Set<User> users = new HashSet<>();

        for (Repository repository : repositoriesMap.values()){
            users.add(repository.getUser());
        }

        users.forEach(user -> {
            System.out.println("Usuario: " + user.getName());
            System.out.println("Cantidad de repositorios: " + user.numberOfRepositories());
            System.out.println("Cantidad de estrellas: " + user.numberOfStars());
            System.out.println(" ----------------- \n");
        });
    }

    public void saveRepositoriesToDB() throws IOException {
        // repositoryRepository.createDB(SQL_FILE_PATH);
        repositoryRepository.saveAll(repositoriesMap.values());
    }
}
