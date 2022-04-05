package com.pims.api.controllers;

import com.pims.api.models.Business;
import com.pims.api.repositories.BusinessRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/business")
public class BusinessController {
    @Autowired
    private BusinessRepository businessRepository;

    @GetMapping
    public List<Business> List() { return businessRepository.findAll(); }
}
