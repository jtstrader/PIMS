package com.pims.api.controllers;

import com.pims.api.models.MaritalStatus;
import com.pims.api.repositories.MaritalStatusRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/marital_status")
public class MaritalStatusController {
    @Autowired
    private MaritalStatusRepository maritalStatusRepository;

    @GetMapping
    public List<MaritalStatus> list() { return maritalStatusRepository.findAll(); }

    @RequestMapping("couples")
    public List<String> getMarriedPeople() { return maritalStatusRepository.getMarriedPeople(); }
}
