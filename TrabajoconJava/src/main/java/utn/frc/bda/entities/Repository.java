package utn.frc.bda.entities;

import jakarta.persistence.*;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Objects;
import java.util.Set;

@Entity @Table(name = "Repository")
public class Repository {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "repository_id")
    private Long id;

    @Column(name = "repository_name")
    private String name;

    @Column(name = "description")
    private String description;

    @Column(name = "last_update")
    private Date lastUpdate;

    @Column(name = "stars")
    private Double stars;

    @Column(name = "url")
    private String url;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "user_name")
    private User user;

    @ManyToMany(cascade = CascadeType.ALL)
    @JoinTable(name = "repository_tag",
            joinColumns = @JoinColumn(name = "repository_id"),
            inverseJoinColumns = @JoinColumn(name = "tag_id"))
    private Set<Tag> tags;

    @ManyToMany(cascade = CascadeType.ALL)
    @JoinTable(name = "repository_language",
            joinColumns = @JoinColumn(name = "repository_id"),
            inverseJoinColumns = @JoinColumn(name = "language_id")
    )
    private Set<Language> languages;


    public Repository(Long id, String name, String description, Date lastUpdate, Double stars, String url, User user, Set<Tag> tags, Set<Language> languages) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.lastUpdate = lastUpdate;
        this.stars = stars;
        this.url = url;
        this.user = user;
        this.tags = tags;
        this.languages = languages;
        user.addRepository(this);
        addRepositoriesToLanguage();
        addRepositoriesToTag();
    }

    public Repository() {
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

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Date getLastUpdate() {
        return lastUpdate;
    }

    public void setLastUpdate(Date lastUpdate) {
        this.lastUpdate = lastUpdate;
    }

    public Double getStars() {
        return stars;
    }

    public void setStars(Double stars) {
        this.stars = stars;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Set<Tag> getTags() {
        return tags;
    }

    public Set<Language> getLanguages() {
        return languages;
    }

    public void setLanguages(Set<Language> languages) {
        this.languages = languages;
    }

    public void setTags(Set<Tag> tags) {
        this.tags = tags;
    }

    public void addRepositoriesToLanguage(){
        languages.forEach(lang -> lang.addRepository(this));
    }

    public void addRepositoriesToTag(){
        tags.forEach(tag -> tag.addRepository(this));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Repository that = (Repository) o;
        return Objects.equals(id, that.id) && Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        int result = Objects.hashCode(id);
        result = 31 * result + Objects.hashCode(name);
        return result;
    }

    @Override
    public String toString() {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
        String formattedDate = lastUpdate != null ? dateFormat.format(lastUpdate) : "null";

        return "Repository{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", lastUpdate=" + formattedDate +
                ", stars=" + stars +
                ", url='" + url + '\'' +
                ", user=" + user +
                ", tags=" + tags +
                ", languages=" + languages +
                '}';
    }
}
