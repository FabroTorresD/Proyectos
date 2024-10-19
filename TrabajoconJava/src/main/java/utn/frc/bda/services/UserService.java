package utn.frc.bda.services;

import utn.frc.bda.entities.User;

import java.util.HashMap;
import java.util.Map;

public class UserService {
    private Map<String, User> usersMap;

    public UserService(){
        this.usersMap = new HashMap<>();
    }

    public User getOrCreateUser(String username){
        if (usersMap.containsKey(username)){
            return usersMap.get(username);
        }

        User user = new User(username);
        usersMap.put(username, user);
        return user;
    }
}
