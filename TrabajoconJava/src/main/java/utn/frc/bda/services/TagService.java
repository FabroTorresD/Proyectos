package utn.frc.bda.services;

import utn.frc.bda.entities.Tag;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class TagService {

    private Map<String, Tag> tagsMap;

    public TagService(){
        tagsMap = new HashMap<>();
    }

    public Set<Tag> getOrCreateTag(String names){

        Set<Tag> tagsResult = new HashSet<>();
        String[] tagsNames = names.split(",");

        for (String tagName : tagsNames){
            if (tagsMap.containsKey(tagName)){
                tagsResult.add(tagsMap.get(tagName));
            } else {
                Tag tag = new Tag(tagName);
                tagsMap.put(tagName, tag);
                tagsResult.add(tag);
            }
        }

        return tagsResult;
    }

}
