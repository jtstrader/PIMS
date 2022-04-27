package com.pims.api.controllers;

import com.pims.api.models.Population;
import com.pims.api.repositories.PopulationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/population")
public class PopulationController {
    @Autowired
    private PopulationRepository populationRepository;

    @GetMapping
    public List<Population> list() { return populationRepository.findAll(); }

    @RequestMapping("{ssn}")
    public Population get(@PathVariable String ssn) { return populationRepository.getById(ssn); }

    @RequestMapping("pop")
    public List<String> listTest() { return populationRepository.getPop(); }
}
