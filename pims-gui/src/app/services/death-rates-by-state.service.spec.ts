import { TestBed } from '@angular/core/testing';

import { DeathRatesByStateService } from './death-rates-by-state.service';

describe('DeathRatesByStateService', () => {
  let service: DeathRatesByStateService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DeathRatesByStateService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
