package utn.frc.bda.services;

import utn.frc.bda.entities.Language;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LanguageService {

    private Map<String, Language> languagesMap;

    public LanguageService(){
        languagesMap = new HashMap<>();
    }

    public Set<Language> getOrCreateLanguage(String names){

        Set<Language> languagesResult = new HashSet<>();
        String[] languagesNames = names.split(",");

        for (String languageName : languagesNames){
            if (languagesMap.containsKey(languageName)){
                languagesResult.add(languagesMap.get(languageName));
            } else {
                Language language = new Language(languageName);
                languagesMap.put(languageName, language);
                languagesResult.add(language);
            }
        }

        return languagesResult;

    }

}
