package com.pims.api.controllers;

import com.pims.api.models.Health;
import com.pims.api.repositories.HealthRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/api/health")
public class HealthController {
    @Autowired
    private HealthRepository healthRepository;

    @GetMapping
    public List<Health> list() { return healthRepository.findAll(); }

    @RequestMapping("death_rate")
    public List<String> getDeathRate() { return healthRepository.getAvgDeathRate(); }

    @RequestMapping("death_ratio")
    public List<String> getDeathRatio() {
        List<String> tempList = healthRepository.getDeathRatio();
        tempList = List.of(tempList.get(0).split(","));
        List<String> retList = new ArrayList<String>();
        retList.add("Population Alive,"+tempList.get(0));
        retList.add("Population Dead,"+tempList.get(1));
        return retList;
    }
}
