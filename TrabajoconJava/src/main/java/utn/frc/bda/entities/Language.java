package utn.frc.bda.entities;

import jakarta.persistence.*;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity @Table(name = "Language")
public class Language {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "language_id")
    private Long id;

    @Column(name = "language_name")
    private String name;

    @ManyToMany(mappedBy = "languages", cascade = CascadeType.ALL)
    private Set<Repository> repositories;

    public Language(String name) {
        this.name = name;
    }

    public Language() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Set<Repository> getRepositories() {
        return repositories;
    }

    public void addRepository(Repository repoToAdd){
        if (repositories == null){
            repositories = new HashSet<>();
        }
        repositories.add(repoToAdd);
    }

    public int numberOfRepositories(){
        return this.repositories.size();
    }

    public Double numberOfStars(){
        Double totalStars = 0.0;

        for (Repository repository : this.repositories) {
            totalStars += repository.getStars();
        }

        return totalStars;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Language language = (Language) o;
        return Objects.equals(id, language.id) && Objects.equals(name, language.name);
    }

    @Override
    public int hashCode() {
        int result = Objects.hashCode(id);
        result = 31 * result + Objects.hashCode(name);
        return result;
    }

    @Override
    public String toString() {
        return "Language{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}
