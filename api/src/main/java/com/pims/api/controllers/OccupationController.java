package com.pims.api.controllers;

import com.pims.api.models.Occupation;
import com.pims.api.repositories.OccupationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/occupation")
public class OccupationController {
    @Autowired
    private OccupationRepository occupationRepository;

    @GetMapping
    public List<Occupation> list() { return occupationRepository.findAll(); }

    @RequestMapping("position_salaries")
    public List<String> getPositionSalaries() { return occupationRepository.averagePositionSalary(); }
}
