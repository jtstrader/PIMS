import { TestBed } from '@angular/core/testing';

import { PopulationDeathRatioService } from './population-death-ratio.service';

describe('PopulationDeathRatioService', () => {
  let service: PopulationDeathRatioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PopulationDeathRatioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
